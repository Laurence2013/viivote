(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let same_qs_ids = new Array();
      let html = '';

      //Object.values(results[0]).forEach(function(q_id){
      //  get_qid = q_id.question_id;
      //});

      results[0].forEach(function(qs_id){
        let get_qid = qs_id.question_id;
        for(let i = 0; i < results[1].length; i++){
          let ques_id = results[1][i].question_id;
          if(get_qid === ques_id){
            same_qs_ids.push(get_qid);
          }
        }
      });

      //for(let i = 0; i < results[0].length; i++){
      //  let get_qid = results[0][i].question_id;
      //}
    
      Object.values(results[1]).forEach(function(qs){
        console.log(same_qs_ids);
        html += '<ul>';
        html += '<div class="results_vote">';
        html += '<li><b>Question: </b>'+ qs.question +'</li>';
        html += '<li><b>Vote A: </b><input type="radio" name="'+ qs.vote_a.questions_vote_id +'" value="'+ qs.vote_a.id +'">'+ qs.vote_a.vote +'</li>';
        html += '<li><b>Vote B: </b><input type="radio" name="'+ qs.vote_b.questions_vote_id +'" value="'+ qs.vote_b.id +'">'+ qs.vote_b.vote +'</li>';
        html += '<li><b>Vote C: </b><input type="radio" name="'+ qs.vote_c.questions_vote_id +'" value="'+ qs.vote_c.id +'">'+ qs.vote_c.vote +'</li>';
        html += '</div>'; 
        html += '<div class="form-group">';
        html += '<li>'+ qs.question_id +'</li>';
        html += '<button class="btn btn-outline-info" type="submit">Vote</button>';
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
