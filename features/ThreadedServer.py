from wsgiref.simple_server import make_server
from os import read, write, pipe, close
from threading import Thread, Event
from select import select


class ThreadedServer():
    """Will provide a temporary test server in another thread for your
    application.
 
    :param app: A wsgi application
    :param host: Listening hostname or IP
    :param port: Listening port preferably >= 1024 unless you're root
    """
    __stop_marker = bytes('stop', 'utf-8')
 
    def __init__(self, app, host='localhost', port=8888):
        self.app = app
        self.host = host
        self.port = port
 
        # Communication pipe with the thread
        self.stop_read, self.stop_write = pipe()
        self.started = False
 
    def __run(self):
        httpd = make_server(self.host, self.port, self.app)
 
        # We don't want logs in the console
        log_request = httpd.RequestHandlerClass.log_request
        no_logging = lambda *args, **kwargs: None
        httpd.RequestHandlerClass.log_request = no_logging
 
        # Notify / unlock self.start()
        self.ready.set()
        while True:
            ready, dummy, dummy = select([httpd, self.stop_read], 
                                         [self.stop_write], 
                                         [])

            # HTTP client request detected ?
            if httpd in ready:
                httpd.handle_request()
 
            # self.stop() synch called ?
            if self.stop_read in ready:
                read(self.stop_read, len(self.__stop_marker))
                
                # Re-enable console logging and exit
                httpd.RequestHandlerClass.log_request = log_request
                break
 
    def start(self):
        """Launches the server in a thread
        """
        # Bounce protection
        if self.started:
            return
 
        # Threaded server and synch setup
        self.ready = Event()
        self.server_thread = Thread(target=self.__run)
        self.server_thread.start()
 
        # Wait server readyness (if a client runs before -> raise URLError)
        self.ready.wait()
        self.started = True
 
    def stop(self):
        """Stops and kills the server and thread
        """
        # Bounce protection
        if not self.started:
            return
 
        # Notify thread's suicide
        write(self.stop_write, self.__stop_marker)
 
        # Cleanup after thread's suicide
        self.server_thread.join()
        close(self.stop_write)
        close(self.stop_read)
        self.started = False
