import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';

  number: JSON;
  total: JSON;
  ids: JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit() { }

  countRows() {
    this.httpClient.get('http://127.0.0.1:5002/').subscribe(data => {
      this.number = data as JSON;
    });
  }

  sumRowData() {
    this.httpClient.get('http://127.0.0.1:5002/rowtotal').subscribe(data => {
      this.total = data as JSON;
    });
  }
  getAllIds() {
    this.httpClient.get('http://127.0.0.1:5002/alldata').subscribe(data => {
      this.ids = data as JSON;
    });
  }
}
