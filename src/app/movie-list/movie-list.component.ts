import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  url = 'http://127.0.0.1:5002/';
  movies = [];
  gotten = false;
  getMovies(): void {
    this.gotten = true;
    this.http.get(this.url + 'movies').toPromise()
      .then(data => {
        console.log(data);
        for (const key in data){
          if (data.hasOwnProperty(key)){
              this.movies.push(data[key]);
          }
        }
      });
  }
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

}
