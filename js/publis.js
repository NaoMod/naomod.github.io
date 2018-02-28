// (function(){

// AJAX helper
function getJSON(url, cb) {
  let xhr = new XMLHttpRequest()
  xhr.open('GET', url)
  xhr.onload = function(e) {
    cb(JSON.parse(this.response))
  }
  xhr.send()
}

// Return HAL API URL augmented with eventual options
function hal(opts = {}) {
  const base_url = "https://api.archives-ouvertes.fr/search/"
  const base_opts = {
    wt: 'json',
    rows: 1000,
    fq: 'structure_t:(naomod OR atlanmodels)',
    fl: ['docid', 'uri_s', 'label_s', 'authFullName_s', 'title_s',
         'producedDateY_i', 'files_s', 'conferenceTitle_s', 'journalTitle_s'
        ].join(','),
    sort: 'producedDateY_i desc',
  }

  const base_opts_str = Object.entries(base_opts).map(([k,v]) => `${k}=${v}`).join('&')
  const opts_str = Object.entries(opts).map(([k,v]) => `&${k}=${v}`).join('')

  return `${base_url}?${base_opts_str}${opts_str}`
}

// Return HTML string from a list of publications object
function publications_to_html(pubs) {
  let html = `<ul class="articles">`
  for (let p of pubs.response.docs) {
    html +=`<li>
              <h4><a href="${p.uri_s}">${p.title_s[0]}</a></h4>
              <p class="name">${p.authFullName_s.join(", ")} (${p.producedDateY_i})</p>
              <p class="venue">${p.conferenceTitle_s || p.journalTitle_s || ""}</p>
              <div class="files">`
    if ("files_s" in p) {
      html += `<a href="${p.files_s[0]}">pdf</a>`
    }
    html += `<a href="${p.uri_s}/bibtex">bibtex</a>
             </div>
             </li>`
  }
  html += "</ul>"
  return html
}

let publications_period = "";

// Update the HTML with the publications object
function update(pubs) {
  document.querySelector('main').innerHTML = publications_to_html(pubs)
}

function publications(start_year, end_year) {
  publications_period = (start_year == end_year ? (" in "+start_year) : (" from "+start_year+" to "+end_year));
  document.querySelector('main').innerHTML = `<p>Loading publications${publications_period}...</p>`
  getJSON(hal({fq: `producedDateY_i:[${start_year} TO ${end_year}]`}), update);
}

// document.querySelector('main').innerHTML = `
// <div class='yearbar'>
//     <button onclick='getPublications()'>All</button>
//     <button onclick='getPublicationsYear(2017,2017)'>2017</button>
//     <button onclick='getPublicationsYear(2016,2016)'>2016</button>
//     <button onclick='getPublicationsYear(2015,2015)'>2015</button>
//     <button onclick='getPublicationsYear(2001,2014)'>Before 2015</button>
// </div>
// <h4>Source: <a href="https://hal.archives-ouvertes.fr/">HAL</a>.</h4>
// `
publications(2017, 2023)

//}());
