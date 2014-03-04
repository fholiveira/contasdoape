gulp = require 'gulp'
gutil = require 'gulp-util'

coffee = require 'gulp-coffee'
stylus = require 'gulp-stylus'
uglify = require 'gulp-uglify'
minifyCSS = require 'gulp-minify-css'
autoprefixer = require 'gulp-autoprefixer'

gulp.task 'compile coffee', ->
  gulp.src './contasdoape/static/coffee/*.coffee'
    .pipe(coffee bare: true)
    .pipe gulp.dest './contasdoape/static/js'

gulp.task 'compile stylus', ->
  gulp.src './contasdoape/static/stylus/*.styl'
    .pipe do stylus
    .pipe do autoprefixer
    .pipe gulp.dest './contasdoape/static/css'

gulp.task 'watch', ->
  gulp.watch './contasdoape/static/stylus/**/*.styl', ['compile stylus']
  gulp.watch './contasdoape/static/coffee/*.coffee', ['compile coffee']

gulp.task 'deploy', ->
  gulp.src('./contasdoape/static/coffee/*.coffee')
    .pipe coffee(bare: true)
    .pipe uglify()
    .pipe gulp.dest './contasdoape/static/js'

  gulp.src './contasdoape/static/stylus/*.styl'
    .pipe do stylus
    .pipe do autoprefixer
    .pipe do minifyCSS
    .pipe gulp.dest './contasdoape/static/css'

gulp.task 'default', ['compile coffee', 'compile stylus', 'watch']
