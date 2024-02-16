import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BannerHelloComponent } from './banner-hello.component';

describe('BannerHelloComponent', () => {
  let component: BannerHelloComponent;
  let fixture: ComponentFixture<BannerHelloComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BannerHelloComponent]
    });
    fixture = TestBed.createComponent(BannerHelloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
