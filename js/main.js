function onJoin() {
  var board = new ChessBoard('chessboard', {
    draggable: true,
    dropOffBoard: 'trash',
    sparePieces: true
  });
  board.start();

  var webrtc = new SimpleWebRTC({
    // the id/element dom element that will hold local video
    localVideoEl: 'localVideo',
    // the id/element dom element that will hold remote videos
    remoteVideosEl: 'removeVideo',
    // immediately ask for camera access
    autoRequestMedia: true
  });

  webrtc.joinRoom('addsheep.classroom.' + $("#roomName")[0].value);

  $("#workspace")[0].style.display = 'block';
  $("#joinRoom")[0].style.display = 'none';
}