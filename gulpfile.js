var gulp = require('gulp');
var minifyCss = require('gulp-csso');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var coffee = require('gulp-coffee');
var order = require('gulp-order');
var merge = require('merge-stream');

var distPath = 'bigData/static/dist';
var customSourcePath = 'bigData/static';

gulp.task('css', function() {
    // create css stream
    return gulp.src([
        // './node_modules/bootstrap/dist/css/bootstrap.min.css'
        customSourcePath + '/css/custom.css',
        customSourcePath + '/css/lobipanel.css'
    ])
        .pipe(concat('app.min.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest(distPath + '/css'));
});

gulp.task('js', function() {
    var coffeeStream = gulp.src('./bigData/static/coffee/*.coffee')
        .pipe(coffee({bare: true}))
        .pipe(concat('coffee-files.js'));

    var jsStream = gulp.src([
        './node_modules/bootstrap/dist/js/bootstrap.min.js',
        'node_modules/jquery-ui/build/release.js',
        customSourcePath + '/js/jquery.ui.touch-punch.js',
        customSourcePath + '/js/lobipanel.js',
        customSourcePath + '/js/faqOverlay.js'
    ]).pipe(concat('js-files.js'));

    merge(jsStream, coffeeStream)
        .pipe(order([
            'js-files.js',
            'coffee-files.js'
        ]))
        .pipe(concat('app.min.js'))
        // .pipe(uglify())
        .pipe(gulp.dest(distPath + '/js'));

    gulp.src('./node_modules/jquery/dist/jquery.min.js')
        .pipe(concat('jquery.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(distPath + '/js'));
});

gulp.task('default', ['css', 'js']);

// development
gulp.task('devChange', function() {
    // watch sass change
    gulp.watch('./bigData/static/css/*.css', ['css']);
    gulp.watch('./bigData/static/js/*.js', ['js']);
    gulp.watch('./bigData/static/coffee/*.coffee', ['js']);
});