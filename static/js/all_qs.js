(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';
      html += '<ul>';
      Object.values(results).forEach(function(qs){
        html += '<input type="hidden" name="'+ qs.user_id +'">';
        html += '<li name="'+ qs.questions_vote +'"><b>Question: </b>'+ qs.question +'</li>';
        html += '<li name="'+ qs.vote_a.id +'"><b>Vote A: </b>'+ qs.vote_a.vote +'</li>';
        html += '<li name="'+ qs.vote_b.id +'"><b>Vote B: </b>'+ qs.vote_b.vote +'</li>';
        html += '<li name="'+ qs.vote_c.id +'"><b>Vote C: </b>'+ qs.vote_c.vote +'</li>';
      });
      html += '</ul>';
      document.getElementById('votes').innerHTML = html;
    }
  }
  http.open('GET', 'all_votes', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
