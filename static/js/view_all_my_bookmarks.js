(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
      let html = '';
      html += '<ul>';
      for(let result in results){
        html += '<b>Question</b>';
        html += '<li>'+ results[result].question +'</li>';
        html += '<b>Votes</b>';
        html += '<li>'+ results[result].vote_a.vote_a.vote +'</li>';
        html += '<li>'+ results[result].vote_b.vote_b.vote +'</li>';
        html += '<li>'+ results[result].vote_c.vote_c.vote +'</li>';
        html += '<small><a href="#">Delete from bookmark</a></small>';
        html += '<hr>';
      }
      html += '</ul>';
      document.getElementById('view_my_bookmarks').innerHTML = html;
    }
  }
  http.open('GET', 'view_my_bookmarks', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
