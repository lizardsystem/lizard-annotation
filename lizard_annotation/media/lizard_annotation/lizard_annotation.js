
function setAnnotations() {
    $("#reference_objects").live('change', function () {
        reference_filter = $("select option:selected").val();
        url = $("#annotation_view_url").val();
        $.ajax({
            type: 'POST',
            url: url,
            data: {reference_filter: reference_filter},
            success: function(val) {
                alert(val);
            },
            error: function(val) {
                alert(val);
            }
        });
         return false;
    });
}

// Initialize all actions.
$(document).ready(function () {
    setAnnotations();
});
