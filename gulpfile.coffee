gulp = require 'gulp'
gutil = require 'gulp-util'

coffee = require 'gulp-coffee'
uglify = require 'gulp-uglify'

gulp.task 'scripts', ->
	gulp.src('./contasdoape/static/coffee/*.coffee')
		.pipe(coffee bare: true, sourceMap: true)
		.pipe(do uglify)
	  .pipe(gulp.dest './contasdoape/static/coffee')

gulp.task 'watch', ->
	gulp.watch './contasdoape/static/coffee/*.coffee', ['scripts']

gulp.task 'default', ['scripts', 'watch']
