(function(){
  function getBaseUrl(){
    let url = location.href;
    let baseURL = url.substring(0, url.indexOf('/', 14));
    if (baseURL.indexOf('http://localhost') != -1) {
        // Base Url for localhost
        let url = location.href;  // window.location.href;
        let pathname = location.pathname;  // window.location.pathname;
        let index1 = url.indexOf(pathname);
        let index2 = url.indexOf("/", index1 + 1);
        let baseLocalUrl = url.substr(0, index2);
        return baseLocalUrl + "/";
    } else {
        // Root Url for domain name
        return baseURL + "/";
    }
  }

  let http = new XMLHttpRequest();
  let base_url = getBaseUrl();
  let answer_vote = 'answer_vote';

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
        if(qs.answers.length > 0){
          html += '<b>All Answers</b>';
          Object.values(qs.answers).forEach(function(qss){
            html += '<li>'+ qss.answer +'</li>';
          });
        }
        html += '</div>'; 
        html += '<div class="form-group">';
        if(qs.has_voted === false){
          html += '<button class="btn btn-outline-info" type="submit">Vote</button>';
        }else{
          html += '<b>You have already voted </b>';
          if(qs.vote_type){
            let vote_type = qs.vote_type;
            if(qs.vote_a_id){ var vote = qs.vote_a_id; }
            if(qs.vote_b_id){ var vote = qs.vote_b_id; }
            if(qs.vote_c_id){ var vote = qs.vote_c_id; }
            html += '<p><a href="'+ base_url + answer_vote + '/'+ qs.question_id + '/' + vote_type + '/' + vote +'">Click here to answer your vote</a></p>';
          }
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
