//https://github.com/trentrichardson/jQuery-Timepicker-Addon

var clock = $('.running-clock');
var clockFormat = 'MMMM D, YYYY h:mm:ssa';
var clockTime = clock.text();
setInterval(clientSideUpdate, 1000);
serverSideUpdate();

var socket = io.connect('/status');
socket.on('applyStatusUpdate', function (data) {
    updateUI(data);
});
$('#light-switch').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    socket.emit('changeStatus', {'lightSwitch': $(this).prop('checked') ? 1 : 0});
});

function updateUI(data) {
    var lightSwitchElement = $('#light-switch');
    (data.relayIsOn) ? lightSwitchElement.prop('checked', 'checked') : lightSwitchElement.prop('checked', '');
}

function serverSideUpdate(){
    setTimeout(function(){
        $.getJSON( "/updateClock", function( data ) {
            if(data){
                clockTime = data.currentTime;
                clock.html(moment.unix(data.currentTime).format(clockFormat));
                serverSideUpdate();
            }
        });
    }, 15000);
}

function clientSideUpdate() {
    clock.css("display", "block");
    clock.html(moment.unix(++clockTime).format(clockFormat));
}
