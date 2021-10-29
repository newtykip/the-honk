const gulp = require('gulp');
const typescript = require('gulp-typescript');
const uglify = require('gulp-uglify');
const rename = require('gulp-rename');

gulp.task('build', () => {
    const tsc = typescript.createProject('tsconfig.json');

    return gulp
        .src('src/**/*.ts')
        .pipe(tsc())
        .pipe(uglify({ mangle: { toplevel: true } }))
        .pipe(
            rename(path => {
                if (path.basename === 'utils') return;
                path.basename = path.basename.substr(0, 1);
            })
        )
        .pipe(gulp.dest('build'));
});
