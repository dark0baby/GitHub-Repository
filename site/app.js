fetch("data/all_news.json")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("news");
    if (!data || data.length === 0) {
      container.innerHTML = "<p>No news yet for today.</p>";
      return;
    }
    data.slice(-10).reverse().forEach(item => {
      const div = document.createElement("div");
      div.className = "card";
      div.innerHTML = `
        <b>${item.what}</b><br/>
        Sector: ${item.sectors.join(", ")}<br/>
        RBI Impact: ${item.rbi_repo}<br/>
        Stocks: ${item.large_cap.join(", ")}
      `;
      container.appendChild(div);
    });
  })
  .catch(err => {
    document.getElementById("news").innerHTML = "<p>Error loading news</p>";
    console.error(err);
  });
