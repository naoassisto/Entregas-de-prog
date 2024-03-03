import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { QuestionService } from './question.service';
import { QuestionBase } from './question-base';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true
})
export class AppComponent implements OnInit {
   title = 'entregastefano';
  questions$!: Observable<QuestionBase<any>[]>;

  constructor(private questionService: QuestionService) { }

  ngOnInit() {
    this.questions$ = this.questionService.getQuestions();
  }
}