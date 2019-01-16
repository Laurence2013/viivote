(function(){
  function getBaseUrl(){
    let url = location.href;
    let baseURL = url.substring(0, url.indexOf('/', 14));
    if (baseURL.indexOf('http://localhost') != -1) {
        let url = location.href;  // window.location.href;
        let pathname = location.pathname;  // window.location.pathname;
        let index1 = url.indexOf(pathname);
        let index2 = url.indexOf("/", index1 + 1);
        let baseLocalUrl = url.substr(0, index2);
        return baseLocalUrl + "/";
    } else {
        return baseURL + "/";
    }
  }
  let base_url = getBaseUrl();
  let set_all_my_questions = 'set_all_my_questions';

  let edit_my_qs = 'edit_my_question'
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';

      Object.values(results).forEach(function(result){
        html += '<ul>';
        let date_updated = result.question.date_updated.slice(0, -14);
        let new_date_format = function(datee){
          let date_split = datee.split("-");
          let year = date_split[0];
          let month = date_split[1];
          let day = date_split[2];
          return day + '/' + month + '/' + year;
        }; 
        html += '<li>'+ result.question.question +' - <small>date added: '+ new_date_format(date_updated) +'</small></li>';
        html +='<li><b>Vote A: </b>'+ result.vote_a.vote +'</li>';
        html +='<li><b>Vote B: </b>'+ result.vote_b.vote +'</li>';
        html +='<li><b>Vote C: </b>'+ result.vote_c.vote +'</li>';

        let find_key = function(f_key){
          let get_key = Object.keys(f_key.question);
          let get_vote = Object.keys(f_key);
          for(let key in get_key){
            if(get_key[key] === 'id'){
              var question_id = f_key.question.id
            }
          }
          for(let vote in get_vote){
            if(get_vote[vote] === 'vote_a'){
              var vote_a_id = f_key.vote_a.id;
            }
          }
          for(let vote in get_vote){
            if(get_vote[vote] === 'vote_b'){
              var vote_b_id = f_key.vote_b.id;
            }
          }
          for(let vote in get_vote){
            if(get_vote[vote] === 'vote_c'){
              var vote_c_id = f_key.vote_c.id;
            }
          }
          html += '<small><a href="'+ base_url + set_all_my_questions + '/' + question_id + '/' + vote_a_id + '/' + vote_b_id + '/' + vote_c_id +'">Edit</a></small> | <small><a href="#">Delete</a></small>';
        };
        find_key(result);
        html += '</ul>';
        html += '<hr>';
      });
      document.getElementById('get_all_questions').innerHTML = html;
    }
  }
  http.open('GET', 'get_all_my_questions', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
