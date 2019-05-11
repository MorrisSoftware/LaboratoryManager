jQuery(function($) {
    var $popup = $('#instr-info-modal');
    $(".instrument-info").on ('click', '.instrument-info-link', function(e) {
        
        e.preventDefault();
        var $link = $(this);
    var popup_url = $link.data('popup-url');

    if (!popup_url) {
    return true;
    }

    $('.modal-body', $popup).load(popup_url, function() {
    $popup.modal("show");
    });
    });
    });
