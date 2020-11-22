import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import {HomepageComponent} from './homepage/homepage.component';
import { MovieListComponent } from './movie-list/movie-list.component';
import { WatchWithFriendsComponent } from './watch-with-friends/watch-with-friends.component';
import { MyRecommendationsComponent } from './my-recommendations/my-recommendations.component';

const routes: Routes = [
  {path: 'homepage', component: HomepageComponent},
  {path: 'movie-list', component: MovieListComponent},
  {path: 'watch-with-friends', component: WatchWithFriendsComponent},
  {path: 'my-recommendations', component: MyRecommendationsComponent},
  {path: '', redirectTo: '/homepage', pathMatch: 'full'}
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
