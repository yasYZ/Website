function addData() {
    const sqlite3 = require('sqlite3').verbose();
    let db = new sqlite3.Database('../../../data2.db');
    let cursor = db.run("CREATE TABLE IF NOT EXISTS data(value TEXT)");

    function dataSaver(value) {
        cursor.run("INSERT INTO data(value) VALUES(?)", value, function(err) {
            if (err) {
                console.log(err.message);
            } else {
                console.log("Entry added to table");
            }
            db.commit()
        });
    }

    // Call dataSaver function with the value to be inserted
    // For example: dataSaver("example value");
}
addData();