(function(){
  let http = new XMLHttpRequest()
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
      let html = '';
      let new_date_format = function(datee){
        let date_split = datee.split("-");
        let year = date_split[0];
        let month = date_split[1];
        let day = date_split[2];
        return day + '/' + month + '/' + year;
      }; 

      Object.values(results).forEach(function(qs){
        Object.values(qs).forEach(function(q){
          let date_updated = q.date_voted.slice(0, -14);
          html += '<ul>';
          html += '<li><b>Question: </b>'+ q.question +' <b>I voted:</b> '+ q.vote +' | <small> voted on </small>'+ new_date_format(date_updated) +'</li>';
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
