import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  movies = ['Toy Story', 'Toy Story 2', 'The Lion King'];
  constructor() { }

  ngOnInit(): void {
  }

}
