import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { AppComponent } from './app.component';
import { HomepageComponent } from './homepage/homepage.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CommonModule } from '@angular/common';
import { MatMenuModule} from '@angular/material/menu';
import { AppRoutingModule } from './app-routing.module';
import { MovieListComponent } from './movie-list/movie-list.component';
import { HttpClientModule} from '@angular/common/http';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MyRecommendationsComponent } from './my-recommendations/my-recommendations.component';
import { WatchWithFriendsComponent } from './watch-with-friends/watch-with-friends.component';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    TopBarComponent,
    MovieListComponent,
    MyRecommendationsComponent,
    WatchWithFriendsComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    CommonModule,
    MatMenuModule,
    AppRoutingModule,
    HttpClientModule,
    MatPaginatorModule,
    MatInputModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
