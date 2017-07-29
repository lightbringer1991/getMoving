var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCss = require('gulp-csso');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var coffee = require('gulp-coffee');
var order = require('gulp-order');
var merge = require('merge-stream');

var distPath = './bigData/static/dist';
var customSourcePath = './bigData/static';

gulp.task('css', function() {
    // create sass stream
    var sassStream = gulp.src(customSourcePath + '/sass/app.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('sass-files.css'));

    // create css stream
    var cssStream = gulp.src([
        // './node_modules/bootstrap/dist/css/bootstrap.min.css',
        customSourcePath + '/css/custom.css',
        customSourcePath + '/lib/lobipanel-v0.7.1/dist/css/lobipanel.min.css'
    ]).pipe(concat('css-files.css'));

    return merge(cssStream, sassStream)
        .pipe(order([
            'css-files.css',
            'sass-files.css'
        ]))
        .pipe(concat('app.min.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest(distPath + '/css'));
});

gulp.task('js', function() {
    var coffeeUtilsStream = gulp.src('./bigData/static/coffee/utils.coffee')
        .pipe(coffee({bare: true}))
        .pipe(concat('coffee-utils.js'));
    var prequisiteStream = gulp.src([
        './node_modules/jquery/dist/jquery.min.js',
        './node_modules/async/dist/async.min.js'
    ]).pipe(concat('prequisite.js'));

    merge(prequisiteStream, coffeeUtilsStream)
        .pipe(order([
            'prequisite.js',
            'coffee-utils.js'
        ]))
        .pipe(concat('prequisite.min.js'))
        // .pipe(uglify())
        .pipe(gulp.dest(distPath + '/js'));


    var coffeeStream = gulp.src('./bigData/static/coffee/app.coffee')
        .pipe(coffee({bare: true}))
        .pipe(concat('coffee-files.js'));

    var jsStream = gulp.src([
        'bigData/static/js/jquery-ui.js',
        customSourcePath + '/js/jquery.ui.touch-punch.js',
        './node_modules/bootstrap/dist/js/bootstrap.min.js',
        customSourcePath + '/lib/lobipanel-v0.7.1/dist/js/lobipanel.min.js',
        customSourcePath + '/js/faqOverlay.js',
        './node_modules/highcharts/highcharts.js'
    ]).pipe(concat('js-files.js'));

    merge(jsStream, coffeeStream)
        .pipe(order([
            'js-files.js',
            'coffee-files.js'
        ]))
        .pipe(concat('app.min.js'))
        // .pipe(uglify())
        .pipe(gulp.dest(distPath + '/js'));
});

gulp.task('copy', function () {
    // copy all bootstrap fonts
    gulp.src(customSourcePath + '/fonts/*')
        .pipe(gulp.dest(distPath + '/fonts'));
});

gulp.task('default', ['css', 'js', 'copy']);


// development
gulp.task('devChange', function() {
    // watch sass change
    gulp.watch('./bigData/static/css/*.css', ['css']);
    gulp.watch('./bigData/static/js/*.js', ['js']);
    gulp.watch('./bigData/static/coffee/*.coffee', ['js']);
});