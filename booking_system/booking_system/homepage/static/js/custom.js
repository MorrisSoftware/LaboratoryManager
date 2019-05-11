$(document).ready(function() {
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
              // Only send the token to relative URLs i.e. locally.
              xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
          }
      }
  });

  var url = '/num_messages';
  get_jsondata(url,show_num_messages);
  });

function show_num_messages(num){
  parsed = JSON.parse(num);
  $('#nummessages').text('(' + parsed + ')');
}

/*Utility functions*/

//get JSON data from server
function get_jsondata(url,callback){
  var promise = $.getJSON(url, function(data){
      callback(data);
  });

  promise.done(function(){
      console.log("Successfully recieved data");
  });
}

// get cookie data
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

// make new element
function elt(name, attributes){
  var node= document.createElement(name);
  if(attributes){
      for (var attr in attributes)
          if(attributes.hasOwnProperty(attr))
              node.setAttribute(attr, attributes[attr]);
  }

  for( var i =2; i < arguments.length; i++){
      var child = arguments[i];
      if(typeof child == "string")
          child = document.createTextNode(child);
      node.appendChild(child);
  }
  return node;
}


//POST new data to server
function post_data(url,data,callback){
  var jqJR = $.post(url,data);
  jqJR.done(function(data){
      callback(data);
  });
}

// destroy DOM element
function destroy_elt(element){
  if($('#'+element)){
      delete $('#'+element);
      $('#'+element).remove();
  }
}