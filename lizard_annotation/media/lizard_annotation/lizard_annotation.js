
function setAnnotations() {
    $("#reference_objects").live('change', function () {
        alert($("select option:selected").val());
        // $.post(
        //     url,
        //     { object_id: object_id },
        //     function (data) {

        //     });
        // return false;
    });
}

// Initialize all actions.
$(document).ready(function () {
    setAnnotations();
});
