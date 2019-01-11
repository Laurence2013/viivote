(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
      let html = '';

      Object.values(results).forEach(function(qs){
        html += '<ul>';
        html += '<div class="results_vote">';
        html += '<li><b>Question: </b>'+ qs.question +'</li>';
        html += '<li><b>Vote A: </b><input type="radio" name="'+ qs.vote_a.questions_vote_id +'" value="'+ qs.vote_a.id +'">'+ qs.vote_a.vote +'</li>';
        html += '<li><b>Vote B: </b><input type="radio" name="'+ qs.vote_b.questions_vote_id +'" value="'+ qs.vote_b.id +'">'+ qs.vote_b.vote +'</li>';
        html += '<li><b>Vote C: </b><input type="radio" name="'+ qs.vote_c.questions_vote_id +'" value="'+ qs.vote_c.id +'">'+ qs.vote_c.vote +'</li>';
        html += '</div>'; 
        html += '<div class="form-group">';
        if(qs.has_voted === false){
          html += '<button class="btn btn-outline-info" type="submit">Vote</button>';
        }else{
          html += '<b>You have already voted </b>';
        }
        html += '</div>';
        html += '</ul>';
      });
      document.getElementById('votes').innerHTML = html;
    }
  }
  http.open('GET', 'all_votes', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
