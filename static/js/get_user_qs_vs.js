(function(){
  let http = new XMLHttpRequest()
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';

      Object.values(results).forEach(function(qs){
        Object.values(qs).forEach(function(q){
          html += '<ul>';
          html += '<li><b>Question: </b>'+ q.question +' <b>I voted:</b> '+ q.vote +'</li>';
          html += '</ul>';
        });
      });
      document.getElementById('all_user_qs_vs').innerHTML = html;
    }
  }
  http.open('GET', 'get_all_user_qs_vs', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
