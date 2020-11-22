import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WatchWithFriendsComponent } from './watch-with-friends.component';

describe('WatchWithFriendsComponent', () => {
  let component: WatchWithFriendsComponent;
  let fixture: ComponentFixture<WatchWithFriendsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WatchWithFriendsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WatchWithFriendsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
