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
  let del_bookmark = 'delete_bookmark';
  let answer_vote = 'answer_vote';
  let edit = 'edit';
  let del_ete = 'delete';

  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let resultss = JSON.parse(http.responseText);
      console.log(resultss);
      let results = resultss.slice(1);
      let html = '';

      html += '<ul>';
      for(let result in results){
        let date_updatedd = results[result].date_updated.slice(0, -14);
        let new_date_format = function(datee){
          let date_split = datee.split("-");
          let year = date_split[0];
          let month = date_split[1];
          let day = date_split[2];
          return day + '/' + month + '/' + year;
        }; 
        html += '<b>Question </b> | <small>'+ new_date_format(date_updatedd) +'</small>';
        html += '<li>'+ results[result].question +' | <small>asked by</small> '+ results[result].username +'</li>';
        html += '<b>Votes</b>';

        html += '<li><b>Vote A: </b><input type="radio" name="'+ results[result].vote_a.qs_id_type +'" value="'+ results[result].vote_a.vote_a.id +'"> '+ results[result].vote_a.vote_a.vote +'</li>';
        html += '<li><b>Vote B: </b><input type="radio" name="'+ results[result].vote_b.qs_id_type +'" value="'+ results[result].vote_b.vote_b.id +'"'+ results[result].vote_a.type +'> '+ results[result].vote_b.vote_b.vote +'</li>';
        html += '<li><b>Vote C: </b><input type="radio" name="'+ results[result].vote_c.qs_id_type +'" value="'+ results[result].vote_c.vote_c.id +'"> '+ results[result].vote_c.vote_c.vote +'</li>';
        if(results[result].answers.ans == null){
          html += '<b>All answers</b>';
          html += '<li>No answers were found so far</li>';
        }else{
          html += '<b>All answers</b>';
          Object.values(results[result].answers.ans).forEach(function(anss){
            let ans_date = anss[0].date_updated.slice(0, -14)
            if(resultss[0].user_id === anss[1].id){
              html += '<li>'+ anss[0].answer +' <small>answered by | '+ anss[1].username +' | '+ new_date_format(ans_date) +' | <a href="'+ base_url + edit + '/' + anss[0].id +'">Edit</a> | <a href="'+ base_url + del_ete + '/' + anss[0].id +'">Delete</a></small></li>';
            }else{
              html += '<li>'+ anss[0].answer +' <small>answered by | '+ anss[1].username +' | '+ new_date_format(ans_date) +'</small></li>';
            }
          });
        }
        if(results[result].has_voted.has_voted === true){
          html += '<p>You voted <b>'+ results[result].has_voted.you_voted.toUpperCase() +'</b></p>';
          html += '<p><a href="'+ base_url + answer_vote + '/' + results[result].question_id +'/'+ results[result].has_voted.you_voted +'/'+ results[result].has_voted.you_voted_for +'">Click here to answer your vote</a></p>'; 
        }else{
          html += '<p><button class="btn btn-outline-info" type="submit">Vote</button></p>';
        }
        html += '<small><a href="'+ base_url + del_bookmark + '/' + results[result].question_id +'">Delete from bookmark</a></small>';
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
