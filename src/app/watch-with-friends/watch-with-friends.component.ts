import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-watch-with-friends',
  templateUrl: './watch-with-friends.component.html',
  styleUrls: ['./watch-with-friends.component.css']
})
export class WatchWithFriendsComponent implements OnInit {
  userID = ['', '', '', ''];
  url = 'http://127.0.0.1:5002/';
  movies = [];
  userId: number;
  pageVal = 1;
  pageOfMovies = [];
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }
  getRecommended(): void{
    this.http.get(this.url + 'recommended/' + this.userID[0] + '/' + this.userID[1] + '/' + this.userID[2] + '/' + this.userID[3])
      .toPromise()
      .then(data => {
        console.log(data);
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
  }
  increasePageNum(): void{
    this.pageVal++;
  }
  decreasePageNum(): void{
    if (this.pageVal >= 1){
      this.pageVal--;
    }
  }

}
