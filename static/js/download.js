function download() {
    excel = new ExcelGen({
        "src_id": "table",
        "show_header": true
    });
    excel.generate();
}
