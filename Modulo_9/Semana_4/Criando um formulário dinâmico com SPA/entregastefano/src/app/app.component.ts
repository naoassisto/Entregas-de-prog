import {Component} from '@angular/core';
import {AsyncPipe} from '@angular/common';

import {DynamicFormComponent} from './DynamicForm/ dynamic-form.component';

import {QuestionService} from './question.service';
import {QuestionBase} from './question-base';
import {Observable} from 'rxjs';

@Component({

  standalone: true,
  selector: 'app-root',
  
  template: `
    <div>
      <h2>Se inscreva para lutar contra um tigre</h2>
      <app-dynamic-form [questions]="questions$ | async"></app-dynamic-form>
    </div>
  `,
  
  
  providers: [QuestionService],
  imports: [AsyncPipe, DynamicFormComponent],
})
export class AppComponent {
  title(title: any) {
    throw new Error('Method not implemented.');
  }
  questions$: Observable<QuestionBase<any>[]>;

  constructor(service: QuestionService) {
    this.questions$ = service.getQuestions();
  }
}