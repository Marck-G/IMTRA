class BackgroundReplace {
    constructor(options) {
        if (options.attribute)
            this.attribute = options.attribute;
        else
            this.attribute = 'bg-img';
        if (options.element)
            this.element = options.element;
        else if (this.attribute)
            this.element = `[${this.attribute}]`;
        if (options.style)
            this.style = options.style;
        else
            this.style = {
                'background-size': 'cover',
                'background-position': 'center center'
            };
    }
    start() {
        $.each($(this.class), (i, element) => {
            let imgUri = $(element).attr(this.attribute);
            $(element).css(this.style);
            $(element).css('background-image', imgUri);
        });
    }
}