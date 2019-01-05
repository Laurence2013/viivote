(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';
      html += '<ul>';
      Object.values(results).forEach(function(qs){
        console.log(qs);
        html += '<li><b>Question: </b>'+ qs.question +'</li>';
        html += '<li><b>Vote A: </b>'+ qs.vote_a +'</li>';
        html += '<li><b>Vote B: </b>'+ qs.vote_b +'</li>';
        html += '<li><b>Vote C: </b>'+ qs.vote_c +'</li>';
      });
      html += '</ul>';
      document.getElementById('votes').innerHTML = html;
    }
  }
  http.open('GET', 'all_votes', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
