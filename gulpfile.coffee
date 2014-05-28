autoprefixer = require 'gulp-autoprefixer'
coffeelint = require 'gulp-coffeelint'
minifyCSS = require 'gulp-minify-css'
plumber = require 'gulp-plumber'
coffee = require 'gulp-coffee'
stylus = require 'gulp-stylus'
uglify = require 'gulp-uglify'
watch = require 'gulp-watch'
clean = require 'gulp-clean'
shell = require 'gulp-shell'
gulp = require 'gulp'

gulp.task 'clean', ->
  gulp.src 'contasdoape/static/js/*', read: false
    .pipe do clean

  gulp.src 'contasdoape/static/css/*', read: false
    .pipe do clean

gulp.task 'lint python', ->
  options =
    glob: '{contasdoape,tests,features}/**/*.py',
    name: 'Python lint'
    verbose: true
    silent: false

  watch options
    .pipe do plumber
    .pipe shell 'pep8 <%= file.path %>'

gulp.task 'compile coffee', ->
  watch glob: 'contasdoape/static/coffee/*.coffee', verbose: true
    .pipe do plumber
    .pipe do coffeelint
    .pipe do coffeelint.reporter
    .pipe coffee { bare: true }
    .pipe gulp.dest 'contasdoape/static/js'

gulp.task 'compile stylus', ->
  watch glob: 'contasdoape/static/stylus/*.styl', verbose: true
    .pipe do plumber
    .pipe do stylus
    .pipe do autoprefixer
    .pipe gulp.dest 'contasdoape/static/css'

gulp.task 'deploy', ['clean'], ->
  gulp.src('contasdoape/static/coffee/*.coffee')
    .pipe do coffeelint
    .pipe coffee { bare: true }
    .pipe do uglify
    .pipe gulp.dest 'contasdoape/static/js'

  gulp.src 'contasdoape/static/stylus/*.styl'
    .pipe do stylus
    .pipe do autoprefixer
    .pipe do minifyCSS
    .pipe gulp.dest 'contasdoape/static/css'

gulp.task 'default',
  ['clean', 'lint python', 'compile coffee', 'compile stylus']
