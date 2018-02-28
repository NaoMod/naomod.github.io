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
    fl: ['uri_s', 'authFullName_s', 'title_s', 'producedDateY_i',
         'files_s', 'conferenceTitle_s', 'journalTitle_s', 'docType_s',
         'citationRef_s'
        ].join(','),
    sort: 'producedDateY_i desc',
  }

  const base_opts_str = Object.entries(base_opts).map(([k,v]) => `${k}=${v}`).join('&')
  const opts_str = Object.entries(opts).map(([k,v]) => `&${k}=${v}`).join('')

  return `${base_url}?${base_opts_str}${opts_str}`
}

// Return the conference name or journal the publication is in,
// or the empty string.
function venue(pub) {
  let v = pub.conferenceTitle_s || pub.journalTitle_s
  // Some articles do not have `journalTitle` set, so extracting it from
  // citationRef seems the only reliable way to get this info.
  if (pub.docType_s === "ART") {
    v = v || pub.citationRef_s.split(',')[0]
  }
  return v || ""
}

// Return a tag identifying the type of the publication (conference, journal,
// preprint, thesis...)
function tag(pub) {
  let type
  switch (pub.docType_s) {
  case 'COMM': type = "Conference"; break
  case 'ART': type = "Journal"; break
  case 'UNDEFINED': type = "Preprint"; break
  case 'THESE': type = "Thesis"; break
  case 'HDR': type = "HDR"; break
  }
  if (type) {
    return `<span class="tag">${type}</span>`
  } else {
    return ""
  }
}

// Return HTML string from a list of publications object
function publications_to_html(pubs) {
  let html = `<ul class="articles">`
  for (let p of pubs.response.docs) {
    html +=`<li>
              <h4><a href="${p.uri_s}">${p.title_s[0]}</a></h4>
              <p class="name">${p.authFullName_s.join(", ")} (${p.producedDateY_i})</p>
              <p class="venue">${venue(p)}</p>${tag(p)}
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
