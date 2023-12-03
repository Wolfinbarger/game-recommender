import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaperPlane, faUser } from "@fortawesome/free-regular-svg-icons";
import {
  faPlus,
  faCircleInfo,
  faChartSimple,
} from "@fortawesome/free-solid-svg-icons";
import { faSteam } from "@fortawesome/free-brands-svg-icons";
import "./card.scss";

export default function Card({ num }) {
  console.log(num);
  return (
    <div className="card">
      <img
        src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
        alt="image of video game"
      />
      <div className="content">
        <header>
          <h2>Game Title #{num}</h2>
          <ul className="card-header-icons">
            <li>
              <FontAwesomeIcon
                icon={faPaperPlane}
                style={{ color: "#fafafa" }}
              />
            </li>
            <li>
              <FontAwesomeIcon icon={faPlus} />
            </li>
            <li>
              <FontAwesomeIcon icon={faCircleInfo} />
            </li>
          </ul>
        </header>
        <div className="info">
          <div className="number-players">
            <FontAwesomeIcon icon={faUser} />
            <p> 1-4 Players</p>
          </div>
          <div className="review-score">
            <FontAwesomeIcon icon={faChartSimple} />

            <p>Review Score 8</p>
          </div>
        </div>
        <div className="description">
          Satisfactory is a first person open-world factory building game with a
          dash of exploration and combat. Play...
        </div>
        <div className="platforms">
          <ul>
            <li>
              <FontAwesomeIcon icon={faSteam} />
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}
