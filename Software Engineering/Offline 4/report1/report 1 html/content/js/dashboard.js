/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 77.14285714285714, "KoPercent": 22.857142857142858};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.7714285714285715, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "/login-1"], "isController": false}, {"data": [1.0, 500, 1500, "/login"], "isController": false}, {"data": [1.0, 500, 1500, "/login-0"], "isController": false}, {"data": [0.98, 500, 1500, "/api/download/256-56"], "isController": false}, {"data": [0.1, 500, 1500, "/courses-39"], "isController": false}, {"data": [0.32, 500, 1500, "/notices"], "isController": false}, {"data": [1.0, 500, 1500, "/"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 350, 80, 22.857142857142858, 124.44000000000004, 19, 484, 69.0, 317.0, 382.9, 462.8800000000001, 3.5398230088495577, 264.6264617572693, 1.8849755056890012], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["/login-1", 50, 0, 0.0, 51.879999999999995, 28, 104, 49.5, 81.89999999999998, 97.89999999999999, 104.0, 0.5101468202548693, 54.31469426901062, 0.2754992105477957], "isController": false}, {"data": ["/login", 50, 0, 0.0, 112.15999999999998, 66, 172, 107.5, 156.29999999999998, 160.35, 172.0, 0.5097931259494897, 54.5329291311086, 0.5351832132770522], "isController": false}, {"data": ["/login-0", 50, 0, 0.0, 59.28, 30, 94, 59.0, 84.6, 86.89999999999999, 94.0, 0.5099491070791135, 0.2559705478893206, 0.2599545252883762], "isController": false}, {"data": ["/api/download/256-56", 50, 1, 2.0, 44.5, 28, 343, 32.5, 65.9, 73.69999999999997, 343.0, 0.5105062179657348, 130.82868480197465, 0.2572472738967961], "isController": false}, {"data": ["/courses-39", 50, 45, 90.0, 276.28, 187, 384, 300.0, 349.0, 375.94999999999993, 384.0, 0.5085900865620328, 22.055624974570495, 0.20015801258251872], "isController": false}, {"data": ["/notices", 50, 34, 68.0, 287.74000000000007, 115, 484, 283.5, 450.9, 469.0, 484.0, 0.5082127175150432, 3.731194541287201, 0.19653538685152058], "isController": false}, {"data": ["/", 50, 0, 0.0, 39.24000000000001, 19, 112, 36.0, 53.9, 83.49999999999987, 112.0, 0.510178052140197, 1.2126693153410542, 0.1753737054231927], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["The operation lasted too long: It took 469 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 386 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 308 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 250 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 380 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 313 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 370 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 301 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 453 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 339 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 289 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 214 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 312 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 484 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 318 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 251 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 299 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 317 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 401 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 404 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 314 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 241 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 224 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 270 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 208 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 343 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 205 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 340 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 388 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 311 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 350 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 385 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 266 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 260 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 382 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 263 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 243 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 222 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 409 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 207 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 424 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 316 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 337 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 217 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 378 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 212 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 352 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 315 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, 5.0, 1.1428571428571428], "isController": false}, {"data": ["The operation lasted too long: It took 336 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 216 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 371 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 457 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 220 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 384 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 262 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 209 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 203 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 2.5, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 432 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 322 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 229 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 226 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 210 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 1.25, 0.2857142857142857], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 350, 80, "The operation lasted too long: It took 315 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 469 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 386 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 308 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 301 milliseconds, but should not have lasted longer than 200 milliseconds.", 2], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["/api/download/256-56", 50, 1, "The operation lasted too long: It took 343 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["/courses-39", 50, 45, "The operation lasted too long: It took 315 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, "The operation lasted too long: It took 316 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 339 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 312 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 318 milliseconds, but should not have lasted longer than 200 milliseconds.", 2], "isController": false}, {"data": ["/notices", 50, 34, "The operation lasted too long: It took 469 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 386 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 388 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 243 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, "The operation lasted too long: It took 308 milliseconds, but should not have lasted longer than 200 milliseconds.", 1], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
