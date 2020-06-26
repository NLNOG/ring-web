<script
    src="https://code.jquery.com/jquery-3.5.0.min.js"
    integrity="sha256-xNzN2a4ltkB44Mc/Jz3pT4iU1cmeR0FkXs4pru/JxaQ="
    crossorigin="anonymous"></script>

<script>
var participants = Array();
$.ajax({
    url: '/scripts/participants.cgi',
    dataType: 'json',
    success: function(response) {
        generate_html(response);
    }
});
function generate_html(data) {
    document.write(data.counters.orgs);
}
</script>
