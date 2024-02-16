import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardAdsComponent } from './card-ads.component';

describe('CardAdsComponent', () => {
  let component: CardAdsComponent;
  let fixture: ComponentFixture<CardAdsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CardAdsComponent]
    });
    fixture = TestBed.createComponent(CardAdsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
