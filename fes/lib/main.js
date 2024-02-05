function make_fes(){
  oevent_name = document.getElementById('event_name');
  oevent_category = document.getElementById('event_category');
  oout = document.getElementById('output');
  oout.style.visibility='visible';

  oevent_description = document.getElementById('event_description');
  oevent_schedule = document.getElementById('event_schedule');
  oevent_map = document.getElementById('event_map');

  if(oevent_category.selectedIndex == 2){
  } else {
    oevent_description.innerHTML = 'このイベント種類は未対応です。';
    oevent_schedule.innerHTML = '';
    oevent_map.innerHTML = '';
    oevent_schedule.innerHTML = '';
    return;
  }


  sret = '';
  sret += oevent_name.value;
  sret += '\r\n'; 
  sret += ' ';
  sret += '地域の物産を楽しみながらマラソンをするイベントです。';
  oevent_description.innerHTML = sret;

  sret = '';
  sret += 'イベント名：';
  sret += oevent_name.value;
  sret += '\r\n'; 
  sret += '日時：';
  sret += '〇〇年〇月〇日 〇時〇分開始';
  sret += '\r\n'; 
  sret += '場所：';
  sret += '〇〇〇〇';
  sret += '\r\n'; 
  oevent_schedule.innerHTML = sret;


  sret = '';
  sret += 'Google MapsのURL';
  oevent_map.innerHTML = sret;

}

