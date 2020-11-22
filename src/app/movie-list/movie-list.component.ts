import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import { Movie } from '../movie';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  pageVal = 1;
  url = 'http://127.0.0.1:5002/';
  pageOfMovies = [];
  movies = [];
  gotten = false;
  getMovies(): void {
    this.gotten = true;
    this.http.get(this.url + 'movies').toPromise()
      .then(data => {
        for (const key in data){
          if (data.hasOwnProperty(key)){
              this.movies.push(data[key]);
          }
        }
      }).then(data => {
        this.onChangePage();
    });
  }
  onChangePage(): void{
    const pageOfMovies = [];
    const maxVal = this.pageVal * 10 - 1 ;
    const minVal = maxVal - 9;
    for (let i = minVal; i <= maxVal; i++){
      pageOfMovies.push(this.movies[i]);
    }
    this.pageOfMovies = pageOfMovies;
    console.log(this.pageOfMovies);
  }
  increasePageNum(): void{
    this.pageVal++;
  }
  decreasePageNum(): void{
    if (this.pageVal >= 1){
      this.pageVal--;
    }
  }

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getMovies();
  }

}
