var socket = io("ws://localhost:5000/", {transports: ['websocket']});
var lightSwitch = $('#light-switch');

lightSwitch.on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    socket.emit('changeStatus', {'lightSwitch': $(this).prop('checked') ? 1 : 0});
});

function updateUI(data) {
    lightSwitch.prop('checked', data.relayIsOn ? 'checked': '');
}

socket.on('applyStatusUpdate', updateUI);