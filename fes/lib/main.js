function make_fes(){
  oevent_name = document.getElementById('event_name');
  oout = document.getElementById('output');
  sret = '';
  sret += oevent_name.value;
  sret += 'が始まるよ'; 
  oout.innerHTML = sret;
}

