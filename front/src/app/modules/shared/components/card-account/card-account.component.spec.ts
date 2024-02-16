import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardAccountComponent } from './card-account.component';

describe('CardAccountComponent', () => {
  let component: CardAccountComponent;
  let fixture: ComponentFixture<CardAccountComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CardAccountComponent]
    });
    fixture = TestBed.createComponent(CardAccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
