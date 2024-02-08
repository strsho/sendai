function make_qr(stag, s){

  c =  document.getElementById(stag);

  return new Promise((res, rej)=> {
    QRCode.toCanvas(c, s, {
      margin: 2, 
      scale: 2
    }, (err, tg) => !err ? res(tg) : res(err));
  });

}


