const pageSize = 50;

let data = {};
let currentPage = 1;

async function loadData() {

    const response = await fetch("data/result.json");

    data = await response.json();

    document.getElementById("update_time").textContent = data.update_time;
    document.getElementById("scan_count").textContent = data.scan_count;
    document.getElementById("count").textContent = data.count + " 檔";

    renderPage(1);

}

function renderPage(page) {

    currentPage = page;

    const stockList = document.getElementById("stock-list");

    stockList.innerHTML = "";

    const start = (page - 1) * pageSize;

    const end = start + pageSize;

    const stocks = data.stocks.slice(start, end);

    stocks.forEach(stock => {

        stockList.innerHTML += `

        <div style="
            border:1px solid #ddd;
            border-radius:10px;
            padding:15px;
            margin:10px 0;
            background:#fff;
        ">

            <h3>${stock.code} ${stock.name}</h3>

            <p>收盤價：${Number(stock.close).toFixed(2)}</p>

            <p>昨日最高：${Number(stock.high).toFixed(2)}</p>

            <p>
    ${stock.osc >= 0 ? "📈" : "📉"} OSC：
    <span
        style="
            color: ${stock.osc >= 0 ? '#d32f2f' : '#2e7d32'};
            font-weight: bold;
        "
    >
        ${Number(stock.osc).toFixed(3)}
    </span>
</p>
        </div>

        `;

    });

    renderPagination();

}

function renderPagination() {

    const totalPages = Math.ceil(data.stocks.length / pageSize);

    let html = "";

    if (currentPage > 1) {

        html += `<button onclick="renderPage(${currentPage - 1})">◀ 上一頁</button>`;

    }

    html += `&nbsp;&nbsp;第 ${currentPage} / ${totalPages} 頁&nbsp;&nbsp;`;

    if (currentPage < totalPages) {

        html += `<button onclick="renderPage(${currentPage + 1})">下一頁 ▶</button>`;

    }

    document.getElementById("pagination").innerHTML = html;

}

loadData();