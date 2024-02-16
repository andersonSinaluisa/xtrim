import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardContactComponent } from './card-contact.component';

describe('CardContactComponent', () => {
  let component: CardContactComponent;
  let fixture: ComponentFixture<CardContactComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CardContactComponent]
    });
    fixture = TestBed.createComponent(CardContactComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
