const pageSize = 50;

let data = {};
let currentPage = 1;

// 所有股票
let allStocks = [];

// 搜尋後股票
let filteredStocks = [];

async function loadData() {

    const response = await fetch("data/result.json");

    data = await response.json();

    allStocks = data.stocks;
    filteredStocks = [...allStocks];

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

    const stocks = filteredStocks.slice(start, end);

    // 沒有搜尋結果
    if (stocks.length === 0) {

        stockList.innerHTML = `
            <div class="no-result">
                🔍 找不到符合條件的股票
            </div>
        `;

        document.getElementById("pagination").innerHTML = "";

        return;

    }

    stocks.forEach(stock => {

        let changeClass = "";

        if (stock.change_percent > 0) {
            changeClass = "osc-up";
        } else if (stock.change_percent < 0) {
            changeClass = "osc-down";
        }

        stockList.innerHTML += `

            <div class="stock-card">

                <h3>${stock.code} ${stock.name}</h3>

                <p>
                    收盤價：
                    <strong>${Number(stock.close).toFixed(2)}</strong>
                </p>

                <p>
                    昨日最高：
                    <strong>${Number(stock.high).toFixed(2)}</strong>
                </p>

                <p>
                    漲跌幅：
                    <span class="${changeClass}">
                        ${Number(stock.change_percent).toFixed(2)}%
                    </span>
                </p>

                <p>
                    OSC：
                    <span class="${stock.osc >= 0 ? "osc-up" : "osc-down"}">
                        ${Number(stock.osc).toFixed(3)}
                    </span>
                </p>

            </div>

        `;

    });

    renderPagination();

}

function renderPagination() {

    const totalPages = Math.ceil(filteredStocks.length / pageSize);

    let html = "";

    // 上一頁
    if (currentPage > 1) {

        html += `
            <button class="page-btn"
                onclick="renderPage(${currentPage - 1})">
                ◀
            </button>
        `;

    }

    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, currentPage + 2);

    if (currentPage <= 3) {
        endPage = Math.min(5, totalPages);
    }

    if (currentPage >= totalPages - 2) {
        startPage = Math.max(1, totalPages - 4);
    }

    for (let i = startPage; i <= endPage; i++) {

        if (i === currentPage) {

            html += `
                <button class="page-btn active">
                    ${i}
                </button>
            `;

        } else {

            html += `
                <button
                    class="page-btn"
                    onclick="renderPage(${i})">
                    ${i}
                </button>
            `;

        }

    }

    // 下一頁
    if (currentPage < totalPages) {

        html += `
            <button class="page-btn"
                onclick="renderPage(${currentPage + 1})">
                ▶
            </button>
        `;

    }

    document.getElementById("pagination").innerHTML = `
        <div class="pagination">
            ${html}
        </div>
    `;

}

function searchStocks() {

    const keyword = document
        .getElementById("search")
        .value
        .trim()
        .toLowerCase();

    if (keyword === "") {

        filteredStocks = [...allStocks];

    } else {

        filteredStocks = allStocks.filter(stock => {

            const code = String(stock.code).toLowerCase();
            const name = String(stock.name).toLowerCase();

            return (
                code.includes(keyword) ||
                name.includes(keyword)
            );

        });

    }

    renderPage(1);

}

loadData();