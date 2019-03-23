module.exports = (grunt) => {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        sass: {
            outStyles: {
                options: {
                    style: 'compressed'
                },
                files: [{

                    src: 'sass/main.scss',
                    dest: 'build/css/main.min.css'

                }]
            }
        },
        uglify: {
            build: {
                src: 'js/*.js',
                dest: 'build/js/main.min.js'
            }
        },
        watch: {
            scripts: {
                files: 'js/*.js',
                task: ['glify'],
                options: {
                    spawn: false
                }
            },
            styles: {
                files: 'sass/*.scss',
                task: ['sass']
            }
        }
    });


    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('minjs', ['uglify']);
    grunt.registerTask('style', ['sass'])
    grunt.registerTask('default', ['sass', 'uglify', 'watch']);

}