odoo.define('product.image.lightbox', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.ProductImageLightbox = publicWidget.Widget.extend({
        selector: '.lightbox-trigger',
        events: {
            'click': '_onImageClick',
        },

        _onImageClick: function(event) {
            event.preventDefault();
            var $target = $(event.currentTarget);
            var options = JSON.parse($target.attr('data-options').replace(/'/g, '"'));
            var imageUrl = $target.attr('href');

            $('body').append(`
                <div id="image-lightbox" class="lightbox">
                    <span class="close" ${options.close ? '' : 'style="display:none"'}>&times;</span>
                    <img class="lightbox-content" src="${imageUrl}" 
                         ${options.zoom_in ? 'data-zoom="true"' : ''}>
                </div>
            `);

            if (options.zoom_in || options.zoom_out) {
                $('.lightbox-content').on('click', function() {
                    $(this).toggleClass('zoomed');
                });
            }

            $('.lightbox .close').on('click', function() {
                $('#image-lightbox').remove();
            });
        },
    });

    return publicWidget.registry.ProductImageLightbox;
});
