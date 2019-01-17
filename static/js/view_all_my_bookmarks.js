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

  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
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
        html += '<li>'+ results[result].question +'</li>';
        html += '<b>Votes</b>';
        html += '<li>'+ results[result].vote_a.vote_a.vote +'</li>';
        html += '<li>'+ results[result].vote_b.vote_b.vote +'</li>';
        html += '<li>'+ results[result].vote_c.vote_c.vote +'</li>';
        if(results[result].answers.ans == null){
          html += '<b>All answers</b>';
          html += '<li>No answers were found so far</li>';
        }else{
          html += '<b>All answers</b>';
          Object.values(results[result].answers.ans).forEach(function(ans){
            html += '<li>'+ ans.answer +'</li>';
          });
        }
        html += '<small><a href="'+ base_url + del_bookmark + '/' + results[result].id +'">Delete from bookmark</a></small>';
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
